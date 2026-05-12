





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String name;
    private String valueSoft;
    private String avatar;
    private String valueHard;
    private String suit;
    private int Count;
    private String rank;



    public Card(
        String name,        String valueSoft,        String avatar,        String valueHard,        String suit,        int Count,        String rank    ) {
        this.name = name;
        this.valueSoft = valueSoft;
        this.avatar = avatar;
        this.valueHard = valueHard;
        this.suit = suit;
        this.Count = Count;
        this.rank = rank;
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
    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }


}