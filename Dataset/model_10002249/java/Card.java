





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String valueHard;
    private String suit;
    private String avatar;
    private String rank;
    private int Count;
    private String name;
    private String valueSoft;





    private Deck deck;




    private Hand hand;


    public Card(
        String valueHard,        String suit,        String avatar,        String rank,        int Count,        String name,        String valueSoft    ) {
        this.valueHard = valueHard;
        this.suit = suit;
        this.avatar = avatar;
        this.rank = rank;
        this.Count = Count;
        this.name = name;
        this.valueSoft = valueSoft;
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
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
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