





import java.util.List;
import java.util.ArrayList;

public class StandardCard  {

    private String suit;
    private None cardName;



    public StandardCard(
        String suit,        None cardName    ) {
        this.suit = suit;
        this.cardName = cardName;
    }


    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public None getCardname() {
        return cardName;
    }

    public void setCardname(None cardName) {
        this.cardName = cardName;
    }


}