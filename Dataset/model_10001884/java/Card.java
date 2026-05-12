





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String name;
    private String strength;
    private int id;





    private Deck deck;


    public Card(
        String name,        String strength,        int id    ) {
        this.name = name;
        this.strength = strength;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}