





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String name;
    private String valueHard;
    private String valueSoft;
    private String rank;
    private int Count;
    private String suit;
    private String avatar;





    private Deck deck;




    private Hand hand;


    public Card(
        String name,        String valueHard,        String valueSoft,        String rank,        int Count,        String suit,        String avatar    ) {
        this.name = name;
        this.valueHard = valueHard;
        this.valueSoft = valueSoft;
        this.rank = rank;
        this.Count = Count;
        this.suit = suit;
        this.avatar = avatar;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValuehard() {
        return valueHard;
    }

    public void setValuehard(String valueHard) {
        this.valueHard = valueHard;
    }
    public String getValuesoft() {
        return valueSoft;
    }

    public void setValuesoft(String valueSoft) {
        this.valueSoft = valueSoft;
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
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }

}