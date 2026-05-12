





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int numMoves;





    private Deck deck;


    public Player(
        int numMoves    ) {
        this.numMoves = numMoves;
    }


    public int getNummoves() {
        return numMoves;
    }

    public void setNummoves(int numMoves) {
        this.numMoves = numMoves;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}