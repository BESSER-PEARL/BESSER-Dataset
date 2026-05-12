





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String avatar;
    private String valueHard;
    private String rank;
    private String valueSoft;
    private String name;
    private String suit;
    private int Count;





    private Hand hand;




    private Deck deck;


    public Card(
        String avatar,        String valueHard,        String rank,        String valueSoft,        String name,        String suit,        int Count    ) {
        this.avatar = avatar;
        this.valueHard = valueHard;
        this.rank = rank;
        this.valueSoft = valueSoft;
        this.name = name;
        this.suit = suit;
        this.Count = Count;
    }


    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getValuehard() {
        return valueHard;
    }

    public void setValuehard(String valueHard) {
        this.valueHard = valueHard;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public int getCount() {
        return Count;
    }

    public void setCount(int Count) {
        this.Count = Count;
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