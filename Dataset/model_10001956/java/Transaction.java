





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int cashondelivery;
    private int debitcard;
    private int creditcard;



    public Transaction(
        int cashondelivery,        int debitcard,        int creditcard    ) {
        this.cashondelivery = cashondelivery;
        this.debitcard = debitcard;
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
    public int getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(int creditcard) {
        this.creditcard = creditcard;
    }


}