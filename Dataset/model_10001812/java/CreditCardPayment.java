





import java.util.List;
import java.util.ArrayList;

public class CreditCardPayment  {

    private String CardType;
    private int CardNumber;



    public CreditCardPayment(
        String CardType,        int CardNumber    ) {
        this.CardType = CardType;
        this.CardNumber = CardNumber;
    }


    public String getCardtype() {
        return CardType;
    }

    public void setCardtype(String CardType) {
        this.CardType = CardType;
    }
    public int getCardnumber() {
        return CardNumber;
    }

    public void setCardnumber(int CardNumber) {
        this.CardNumber = CardNumber;
    }


}