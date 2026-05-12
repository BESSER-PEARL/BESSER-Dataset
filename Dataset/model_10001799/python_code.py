from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class felhaszn_l__Actor:

    pass





class Persistence:

    pass


class Class:

    pass


class SaveGameWidget:

    def __init__(self, okButton: str, cancelButton: str, _listWidget: str, class5: "Class" = None):
        self.okButton = okButton
        self.cancelButton = cancelButton
        self._listWidget = _listWidget
        self.class5 = class5
        
        pass
    @property
    def okButton(self):
        return self.__okButton
    @okButton.setter
    def okButton(self, okButton: str):
        self.__okButton = okButton

    @property
    def _listWidget(self):
        return self.___listWidget
    @_listWidget.setter
    def _listWidget(self, _listWidget: str):
        self.___listWidget = _listWidget

    @property
    def cancelButton(self):
        return self.__cancelButton
    @cancelButton.setter
    def cancelButton(self, cancelButton: str):
        self.__cancelButton = cancelButton

    @property
    def class5(self):
        return self.__class5
    @class5.setter
    def class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SaveGameWidget__class5", None)
        self.__class5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "saveGameWidget4"):
                opp_val = getattr(old_value, "saveGameWidget4", None)
                if opp_val == self:
                    setattr(old_value, "saveGameWidget4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "saveGameWidget4"):
                opp_val = getattr(value, "saveGameWidget4", None)
                setattr(value, "saveGameWidget4", self)



class LoadGameWidget:

    pass


class Model:

    def __init__(self, gameTable: str, gameSize: str, steps: str, playerNr: str, gameOver: bool, pl1points: str, pl2points: str, selected: str, goodselected: bool, pl1: str, pl2: str, class3: "Class" = None, _dataAccess6: "Persistence" = None):
        self.gameTable = gameTable
        self.gameSize = gameSize
        self.steps = steps
        self.playerNr = playerNr
        self.gameOver = gameOver
        self.pl1points = pl1points
        self.pl2points = pl2points
        self.selected = selected
        self.goodselected = goodselected
        self.pl1 = pl1
        self.pl2 = pl2
        self.class3 = class3
        self._dataAccess6 = _dataAccess6
        
        pass
    @property
    def pl1(self):
        return self.__pl1
    @pl1.setter
    def pl1(self, pl1: str):
        self.__pl1 = pl1

    @property
    def gameSize(self):
        return self.__gameSize
    @gameSize.setter
    def gameSize(self, gameSize: str):
        self.__gameSize = gameSize

    @property
    def playerNr(self):
        return self.__playerNr
    @playerNr.setter
    def playerNr(self, playerNr: str):
        self.__playerNr = playerNr

    @property
    def gameOver(self):
        return self.__gameOver
    @gameOver.setter
    def gameOver(self, gameOver: bool):
        self.__gameOver = gameOver

    @property
    def pl2(self):
        return self.__pl2
    @pl2.setter
    def pl2(self, pl2: str):
        self.__pl2 = pl2

    @property
    def selected(self):
        return self.__selected
    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def gameTable(self):
        return self.__gameTable
    @gameTable.setter
    def gameTable(self, gameTable: str):
        self.__gameTable = gameTable

    @property
    def goodselected(self):
        return self.__goodselected
    @goodselected.setter
    def goodselected(self, goodselected: bool):
        self.__goodselected = goodselected

    @property
    def pl1points(self):
        return self.__pl1points
    @pl1points.setter
    def pl1points(self, pl1points: str):
        self.__pl1points = pl1points

    @property
    def steps(self):
        return self.__steps
    @steps.setter
    def steps(self, steps: str):
        self.__steps = steps

    @property
    def pl2points(self):
        return self.__pl2points
    @pl2points.setter
    def pl2points(self, pl2points: str):
        self.__pl2points = pl2points

    @property
    def class3(self):
        return self.__class3
    @class3.setter
    def class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model__class3", None)
        self.__class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model2"):
                opp_val = getattr(old_value, "model2", None)
                if opp_val == self:
                    setattr(old_value, "model2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model2"):
                opp_val = getattr(value, "model2", None)
                setattr(value, "model2", self)

    @property
    def _dataAccess6(self):
        return self.___dataAccess6
    @_dataAccess6.setter
    def _dataAccess6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Model___dataAccess6", None)
        self.___dataAccess6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model7"):
                opp_val = getattr(old_value, "model7", None)
                if opp_val == self:
                    setattr(old_value, "model7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model7"):
                opp_val = getattr(value, "model7", None)
                setattr(value, "model7", self)

