





import java.util.List;
import java.util.ArrayList;

public class Strategy  {

    private None game;





    private BlackjackGame blackjackgame;


    public Strategy(
        None game    ) {
        this.game = game;
    }


    public None getGame() {
        return game;
    }

    public void setGame(None game) {
        this.game = game;
    }

    public BlackjackGame getBlackjackgame() {
        return blackjackgame;
    }

    public void setBlackjackgame(BlackjackGame blackjackgame) {
        this.blackjackgame = blackjackgame;
    }

}