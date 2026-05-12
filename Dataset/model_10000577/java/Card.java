





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String valueHard;
    private String suit;
    private String valueSoft;
    private String avatar;
    private String rank;
    private int Count;
    private String name;



    public Card(
        String valueHard,        String suit,        String valueSoft,        String avatar,        String rank,        int Count,        String name    ) {
        this.valueHard = valueHard;
        this.suit = suit;
        this.valueSoft = valueSoft;
        this.avatar = avatar;
        this.rank = rank;
        this.Count = Count;
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


}