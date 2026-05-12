





import java.util.List;
import java.util.ArrayList;

public class Game_PlayerBoard  {

    private int PlayerID;
    private None ColonistZone;



    public Game_PlayerBoard(
        int PlayerID,        None ColonistZone    ) {
        this.PlayerID = PlayerID;
        this.ColonistZone = ColonistZone;
    }


    public int getPlayerid() {
        return PlayerID;
    }

    public void setPlayerid(int PlayerID) {
        this.PlayerID = PlayerID;
    }
    public None getColonistzone() {
        return ColonistZone;
    }

    public void setColonistzone(None ColonistZone) {
        this.ColonistZone = ColonistZone;
    }


}