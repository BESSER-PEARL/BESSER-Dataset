





import java.util.List;
import java.util.ArrayList;

public class GameBoard  {

    private String garbagePile;
    private String discardPile;
    private String shelf;





    private Deck deck;


    public GameBoard(
        String garbagePile,        String discardPile,        String shelf    ) {
        this.garbagePile = garbagePile;
        this.discardPile = discardPile;
        this.shelf = shelf;
    }


    public String getGarbagepile() {
        return garbagePile;
    }

    public void setGarbagepile(String garbagePile) {
        this.garbagePile = garbagePile;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getShelf() {
        return shelf;
    }

    public void setShelf(String shelf) {
        this.shelf = shelf;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}