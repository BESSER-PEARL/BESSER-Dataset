





import java.util.List;
import java.util.ArrayList;

public class ElevensGame  {

    private int Board_9_;
    private boolean win;





    private Player player;




    private Deck deck;


    public ElevensGame(
        int Board_9_,        boolean win    ) {
        this.Board_9_ = Board_9_;
        this.win = win;
    }


    public int getBoard_9_() {
        return Board_9_;
    }

    public void setBoard_9_(int Board_9_) {
        this.Board_9_ = Board_9_;
    }
    public boolean getWin() {
        return win;
    }

    public void setWin(boolean win) {
        this.win = win;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}