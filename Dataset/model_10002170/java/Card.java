





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None cardValue;
    private None suit;



    public Card(
        None cardValue,        None suit    ) {
        this.cardValue = cardValue;
        this.suit = suit;
    }


    public None getCardvalue() {
        return cardValue;
    }

    public void setCardvalue(None cardValue) {
        this.cardValue = cardValue;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }


}