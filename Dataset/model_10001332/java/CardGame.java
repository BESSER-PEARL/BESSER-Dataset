





import java.util.List;
import java.util.ArrayList;

public class CardGame  {

    private int CardNumber;
    private String suit;



    public CardGame(
        int CardNumber,        String suit    ) {
        this.CardNumber = CardNumber;
        this.suit = suit;
    }


    public int getCardnumber() {
        return CardNumber;
    }

    public void setCardnumber(int CardNumber) {
        this.CardNumber = CardNumber;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}