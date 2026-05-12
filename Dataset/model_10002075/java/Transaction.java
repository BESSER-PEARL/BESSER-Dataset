





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int debitcard;
    private int cashondelivery;
    private int creditcard;



    public Transaction(
        int debitcard,        int cashondelivery,        int creditcard    ) {
        this.debitcard = debitcard;
        this.cashondelivery = cashondelivery;
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
    public int getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(int creditcard) {
        this.creditcard = creditcard;
    }


}