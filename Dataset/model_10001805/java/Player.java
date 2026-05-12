





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None hand;
    private int points;





    private Deck deck;




    private GameBoard gameboard;


    public Player(
        None hand,        int points    ) {
        this.hand = hand;
        this.points = points;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public GameBoard getGameboard() {
        return gameboard;
    }

    public void setGameboard(GameBoard gameboard) {
        this.gameboard = gameboard;
    }

}