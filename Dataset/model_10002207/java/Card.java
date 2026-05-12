





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String faceValue;
    private int value;
    private String suit;



    public Card(
        String faceValue,        int value,        String suit    ) {
        this.faceValue = faceValue;
        this.value = value;
        this.suit = suit;
    }


    public String getFacevalue() {
        return faceValue;
    }

    public void setFacevalue(String faceValue) {
        this.faceValue = faceValue;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}