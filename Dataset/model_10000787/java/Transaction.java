





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int creditcard;
    private int cashondelivery;
    private int debitcard;



    public Transaction(
        int creditcard,        int cashondelivery,        int debitcard    ) {
        this.creditcard = creditcard;
        this.cashondelivery = cashondelivery;
        this.debitcard = debitcard;
    }


    public int getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(int creditcard) {
        this.creditcard = creditcard;
    }
    public int getCashondelivery() {
        return cashondelivery;
    }

    public void setCashondelivery(int cashondelivery) {
        this.cashondelivery = cashondelivery;
    }
    public int getDebitcard() {
        return debitcard;
    }

    public void setDebitcard(int debitcard) {
        this.debitcard = debitcard;
    }


}