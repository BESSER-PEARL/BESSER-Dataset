





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String ID;
    private int bet;





    private Deck deck;


    public Player(
        String ID,        int bet    ) {
        this.ID = ID;
        this.bet = bet;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}