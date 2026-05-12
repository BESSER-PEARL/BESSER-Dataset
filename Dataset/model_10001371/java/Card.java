





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private int Count;
    private String valueSoft;
    private String avatar;
    private String suit;
    private String valueHard;
    private String name;





    private HandDeck handdeck;




    private Deck deck;


    public Card(
        String rank,        int Count,        String valueSoft,        String avatar,        String suit,        String valueHard,        String name    ) {
        this.rank = rank;
        this.Count = Count;
        this.valueSoft = valueSoft;
        this.avatar = avatar;
        this.suit = suit;
        this.valueHard = valueHard;
        this.name = name;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public int getCount() {
        return Count;
    }

    public void setCount(int Count) {
        this.Count = Count;
    }
    public String getValuesoft() {
        return valueSoft;
    }

    public void setValuesoft(String valueSoft) {
        this.valueSoft = valueSoft;
    }
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public String getValuehard() {
        return valueHard;
    }

    public void setValuehard(String valueHard) {
        this.valueHard = valueHard;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HandDeck getHanddeck() {
        return handdeck;
    }

    public void setHanddeck(HandDeck handdeck) {
        this.handdeck = handdeck;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}