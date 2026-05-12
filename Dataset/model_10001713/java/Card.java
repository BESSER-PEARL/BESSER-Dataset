





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String cardholderName;
    private boolean isCredit;
    private int cardSN;
    private boolean isDebit;
    private int cardNumber;



    public Card(
        String cardholderName,        boolean isCredit,        int cardSN,        boolean isDebit,        int cardNumber    ) {
        this.cardholderName = cardholderName;
        this.isCredit = isCredit;
        this.cardSN = cardSN;
        this.isDebit = isDebit;
        this.cardNumber = cardNumber;
    }


    public String getCardholdername() {
        return cardholderName;
    }

    public void setCardholdername(String cardholderName) {
        this.cardholderName = cardholderName;
    }
    public boolean getIscredit() {
        return isCredit;
    }

    public void setIscredit(boolean isCredit) {
        this.isCredit = isCredit;
    }
    public int getCardsn() {
        return cardSN;
    }

    public void setCardsn(int cardSN) {
        this.cardSN = cardSN;
    }
    public boolean getIsdebit() {
        return isDebit;
    }

    public void setIsdebit(boolean isDebit) {
        this.isDebit = isDebit;
    }
    public int getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(int cardNumber) {
        this.cardNumber = cardNumber;
    }


}