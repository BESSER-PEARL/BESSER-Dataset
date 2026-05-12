





import java.util.List;
import java.util.ArrayList;

public class PlayingCard  {

    private boolean faceUp;





    private Deck deck;


    public PlayingCard(
        boolean faceUp    ) {
        this.faceUp = faceUp;
    }


    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}