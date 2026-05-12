





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int creditcard;
    private int debitcard;
    private int cashondelivery;



    public Transaction(
        int creditcard,        int debitcard,        int cashondelivery    ) {
        this.creditcard = creditcard;
        this.debitcard = debitcard;
        this.cashondelivery = cashondelivery;
    }


    public int getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(int creditcard) {
        this.creditcard = creditcard;
    }
    public int getDebitcard() {
        return debitcard;
    }

    public void setDebitcard(int debitcard) {
        this.debitcard = debitcard;
    }
    public int getCashondelivery() {
        return cashondelivery;
    }

    public void setCashondelivery(int cashondelivery) {
        this.cashondelivery = cashondelivery;
    }


}