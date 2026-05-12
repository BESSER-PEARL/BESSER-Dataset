





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int Count;
    private String rank;
    private String valueSoft;
    private String valueHard;
    private String name;
    private String avatar;
    private String suit;





    private Hand hand;




    private Deck deck;


    public Card(
        int Count,        String rank,        String valueSoft,        String valueHard,        String name,        String avatar,        String suit    ) {
        this.Count = Count;
        this.rank = rank;
        this.valueSoft = valueSoft;
        this.valueHard = valueHard;
        this.name = name;
        this.avatar = avatar;
        this.suit = suit;
    }


    public int getCount() {
        return Count;
    }

    public void setCount(int Count) {
        this.Count = Count;
    }
    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public String getValuesoft() {
        return valueSoft;
    }

    public void setValuesoft(String valueSoft) {
        this.valueSoft = valueSoft;
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

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}