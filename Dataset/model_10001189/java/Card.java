





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private String name;
    private int Count;
    private String avatar;
    private String valueSoft;
    private String valueHard;
    private String suit;





    private Hand hand;




    private Deck deck;


    public Card(
        String rank,        String name,        int Count,        String avatar,        String valueSoft,        String valueHard,        String suit    ) {
        this.rank = rank;
        this.name = name;
        this.Count = Count;
        this.avatar = avatar;
        this.valueSoft = valueSoft;
        this.valueHard = valueHard;
        this.suit = suit;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
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
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
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