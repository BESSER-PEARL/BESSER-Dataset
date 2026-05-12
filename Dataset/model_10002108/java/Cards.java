





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private int num;
    private None suit;
    private int power;
    private int value;



    public Cards(
        int num,        None suit,        int power,        int value    ) {
        this.num = num;
        this.suit = suit;
        this.power = power;
        this.value = value;
    }


    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}