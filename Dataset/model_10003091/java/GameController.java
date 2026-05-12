





import java.util.List;
import java.util.ArrayList;

public class GameController  {

    private None gameView;
    private None cardGame;





    private CardGame cardgame;




    private GameBoard gameboard;


    public GameController(
        None gameView,        None cardGame    ) {
        this.gameView = gameView;
        this.cardGame = cardGame;
    }


    public None getGameview() {
        return gameView;
    }

    public void setGameview(None gameView) {
        this.gameView = gameView;
    }
    public None getCardgame() {
        return cardGame;
    }

    public void setCardgame(None cardGame) {
        this.cardGame = cardGame;
    }

    public CardGame getCardgame() {
        return cardgame;
    }

    public void setCardgame(CardGame cardgame) {
        this.cardgame = cardgame;
    }
    public GameBoard getGameboard() {
        return gameboard;
    }

    public void setGameboard(GameBoard gameboard) {
        this.gameboard = gameboard;
    }

}