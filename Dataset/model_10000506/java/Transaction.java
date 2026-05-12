





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int cashondelivery;



    public Transaction(
        int cashondelivery    ) {
        this.cashondelivery = cashondelivery;
    }


    public int getCashondelivery() {
        return cashondelivery;
    }

    public void setCashondelivery(int cashondelivery) {
        this.cashondelivery = cashondelivery;
    }


}