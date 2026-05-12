





import java.util.List;
import java.util.ArrayList;

public class GameSession  {

    private String GameSession_Game_;
    private String setPlayers__;
    private String GameSession_Game__Card_;



    public GameSession(
        String GameSession_Game_,        String setPlayers__,        String GameSession_Game__Card_    ) {
        this.GameSession_Game_ = GameSession_Game_;
        this.setPlayers__ = setPlayers__;
        this.GameSession_Game__Card_ = GameSession_Game__Card_;
    }


    public String getGamesession_game_() {
        return GameSession_Game_;
    }

    public void setGamesession_game_(String GameSession_Game_) {
        this.GameSession_Game_ = GameSession_Game_;
    }
    public String getSetplayers__() {
        return setPlayers__;
    }

    public void setSetplayers__(String setPlayers__) {
        this.setPlayers__ = setPlayers__;
    }
    public String getGamesession_game__card_() {
        return GameSession_Game__Card_;
    }

    public void setGamesession_game__card_(String GameSession_Game__Card_) {
        this.GameSession_Game__Card_ = GameSession_Game__Card_;
    }


}