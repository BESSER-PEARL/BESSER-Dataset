





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String int;
    private String Card;
    private String Deck;
    private String int1;



    public Player(
        String int,        String Card,        String Deck,        String int1    ) {
        this.int = int;
        this.Card = Card;
        this.Deck = Deck;
        this.int1 = int1;
    }


    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }
    public String getCard() {
        return Card;
    }

    public void setCard(String Card) {
        this.Card = Card;
    }
    public String getDeck() {
        return Deck;
    }

    public void setDeck(String Deck) {
        this.Deck = Deck;
    }
    public String getInt1() {
        return int1;
    }

    public void setInt1(String int1) {
        this.int1 = int1;
    }


}