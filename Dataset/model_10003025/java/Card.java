





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String valueSoft;
    private String avatar;
    private int Count;
    private String name;
    private String valueHard;
    private String suit;
    private String rank;





    private Hand hand;




    private Deck deck;


    public Card(
        String valueSoft,        String avatar,        int Count,        String name,        String valueHard,        String suit,        String rank    ) {
        this.valueSoft = valueSoft;
        this.avatar = avatar;
        this.Count = Count;
        this.name = name;
        this.valueHard = valueHard;
        this.suit = suit;
        this.rank = rank;
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
    public int getCount() {
        return Count;
    }

    public void setCount(int Count) {
        this.Count = Count;
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
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
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