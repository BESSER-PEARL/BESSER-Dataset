





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private String Character;
    private String Suit;





    private Deck deck;


    public Cards(
        String Character,        String Suit    ) {
        this.Character = Character;
        this.Suit = Suit;
    }


    public String getCharacter() {
        return Character;
    }

    public void setCharacter(String Character) {
        this.Character = Character;
    }
    public String getSuit() {
        return Suit;
    }

    public void setSuit(String Suit) {
        this.Suit = Suit;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}