





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private String valueSoft;
    private String valueHard;
    private int Count;
    private String suit;
    private String avatar;
    private String name;





    private Hand hand;


    public Card(
        String rank,        String valueSoft,        String valueHard,        int Count,        String suit,        String avatar,        String name    ) {
        this.rank = rank;
        this.valueSoft = valueSoft;
        this.valueHard = valueHard;
        this.Count = Count;
        this.suit = suit;
        this.avatar = avatar;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }

}