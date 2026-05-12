





import java.util.List;
import java.util.ArrayList;

public class StandardCard  {

    private boolean standardCard;
    private String suit;
    private None cardName;



    public StandardCard(
        boolean standardCard,        String suit,        None cardName    ) {
        this.standardCard = standardCard;
        this.suit = suit;
        this.cardName = cardName;
    }


    public boolean getStandardcard() {
        return standardCard;
    }

    public void setStandardcard(boolean standardCard) {
        this.standardCard = standardCard;
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