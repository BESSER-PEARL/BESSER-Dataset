





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private int cardValue;
    private String cardName;



    public Cards(
        int cardValue,        String cardName    ) {
        this.cardValue = cardValue;
        this.cardName = cardName;
    }


    public int getCardvalue() {
        return cardValue;
    }

    public void setCardvalue(int cardValue) {
        this.cardValue = cardValue;
    }
    public String getCardname() {
        return cardName;
    }

    public void setCardname(String cardName) {
        this.cardName = cardName;
    }


}