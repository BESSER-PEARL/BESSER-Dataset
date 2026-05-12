





import java.util.List;
import java.util.ArrayList;

public class War_Card1  {

    private None suit;
    private None rank1;
    private int value1;
    private int value;
    private None suit1;
    private None rank;



    public War_Card1(
        None suit,        None rank1,        int value1,        int value,        None suit1,        None rank    ) {
        this.suit = suit;
        this.rank1 = rank1;
        this.value1 = value1;
        this.value = value;
        this.suit1 = suit1;
        this.rank = rank;
    }


    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getRank1() {
        return rank1;
    }

    public void setRank1(None rank1) {
        this.rank1 = rank1;
    }
    public int getValue1() {
        return value1;
    }

    public void setValue1(int value1) {
        this.value1 = value1;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public None getSuit1() {
        return suit1;
    }

    public void setSuit1(None suit1) {
        this.suit1 = suit1;
    }
    public None getRank() {
        return rank;
    }

    public void setRank(None rank) {
        this.rank = rank;
    }


}