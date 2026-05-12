





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int Number;
    private String Suit;



    public Card(
        int Number,        String Suit    ) {
        this.Number = Number;
        this.Suit = Suit;
    }


    public int getNumber() {
        return Number;
    }

    public void setNumber(int Number) {
        this.Number = Number;
    }
    public String getSuit() {
        return Suit;
    }

    public void setSuit(String Suit) {
        this.Suit = Suit;
    }


}