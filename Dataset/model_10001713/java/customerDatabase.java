





import java.util.List;
import java.util.ArrayList;

public class customerDatabase  {

    private int creditCardNum;
    private String paymentHistory;
    private String customerName;
    private int SUID;





    private List<Card> cards;


    public customerDatabase(
        int creditCardNum,        String paymentHistory,        String customerName,        int SUID    ) {
        this.creditCardNum = creditCardNum;
        this.paymentHistory = paymentHistory;
        this.customerName = customerName;
        this.SUID = SUID;
        this.cards = new ArrayList<>();
    }

    public customerDatabase(
        int creditCardNum,        String paymentHistory,        String customerName,        int SUID        ArrayList<Card> cards    ) {
        this.creditCardNum = creditCardNum;
        this.paymentHistory = paymentHistory;
        this.customerName = customerName;
        this.SUID = SUID;
        this.cards = cards;
    }

    public int getCreditcardnum() {
        return creditCardNum;
    }

    public void setCreditcardnum(int creditCardNum) {
        this.creditCardNum = creditCardNum;
    }
    public String getPaymenthistory() {
        return paymentHistory;
    }

    public void setPaymenthistory(String paymentHistory) {
        this.paymentHistory = paymentHistory;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public int getSuid() {
        return SUID;
    }

    public void setSuid(int SUID) {
        this.SUID = SUID;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}