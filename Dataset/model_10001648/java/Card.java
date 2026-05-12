





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int cardFace;
    private String cardSuit;



    public Card(
        int cardFace,        String cardSuit    ) {
        this.cardFace = cardFace;
        this.cardSuit = cardSuit;
    }


    public int getCardface() {
        return cardFace;
    }

    public void setCardface(int cardFace) {
        this.cardFace = cardFace;
    }
    public String getCardsuit() {
        return cardSuit;
    }

    public void setCardsuit(String cardSuit) {
        this.cardSuit = cardSuit;
    }


}