





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String color;
    private int number;
    private String suit;



    public Card(
        String color,        int number,        String suit    ) {
        this.color = color;
        this.number = number;
        this.suit = suit;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}