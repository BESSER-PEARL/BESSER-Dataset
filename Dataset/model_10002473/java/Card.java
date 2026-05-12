





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String avatar;
    private String rank;
    private String suit;
    private String valueSoft;
    private int Count;
    private String name;
    private String valueHard;





    private Deck deck;




    private Hand hand;


    public Card(
        String avatar,        String rank,        String suit,        String valueSoft,        int Count,        String name,        String valueHard    ) {
        this.avatar = avatar;
        this.rank = rank;
        this.suit = suit;
        this.valueSoft = valueSoft;
        this.Count = Count;
        this.name = name;
        this.valueHard = valueHard;
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
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public String getValuesoft() {
        return valueSoft;
    }

    public void setValuesoft(String valueSoft) {
        this.valueSoft = valueSoft;
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