





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String avatar;
    private String name;
    private int Count;
    private String rank;
    private String valueSoft;
    private String suit;
    private String valueHard;





    private Deck deck;




    private Hand hand;


    public Card(
        String avatar,        String name,        int Count,        String rank,        String valueSoft,        String suit,        String valueHard    ) {
        this.avatar = avatar;
        this.name = name;
        this.Count = Count;
        this.rank = rank;
        this.valueSoft = valueSoft;
        this.suit = suit;
        this.valueHard = valueHard;
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