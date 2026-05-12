





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int Count;
    private String avatar;
    private String name;
    private String valueSoft;
    private String suit;
    private String valueHard;
    private String rank;





    private Hand hand;




    private Deck deck;


    public Card(
        int Count,        String avatar,        String name,        String valueSoft,        String suit,        String valueHard,        String rank    ) {
        this.Count = Count;
        this.avatar = avatar;
        this.name = name;
        this.valueSoft = valueSoft;
        this.suit = suit;
        this.valueHard = valueHard;
        this.rank = rank;
    }


    public int getCount() {
        return Count;
    }

    public void setCount(int Count) {
        this.Count = Count;
    }
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValuesoft() {
        return valueSoft;
    }

    public void setValuesoft(String valueSoft) {
        this.valueSoft = valueSoft;
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
    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
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