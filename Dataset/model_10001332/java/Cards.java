





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private None card;
    private String attribute3;
    private int attribute2;





    private CardGame cardgame;


    public Cards(
        None card,        String attribute3,        int attribute2    ) {
        this.card = card;
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
    }


    public None getCard() {
        return card;
    }

    public void setCard(None card) {
        this.card = card;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public int getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(int attribute2) {
        this.attribute2 = attribute2;
    }

    public CardGame getCardgame() {
        return cardgame;
    }

    public void setCardgame(CardGame cardgame) {
        this.cardgame = cardgame;
    }

}