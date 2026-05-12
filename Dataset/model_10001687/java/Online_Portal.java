





import java.util.List;
import java.util.ArrayList;

public class Online_Portal  {

    private String StoreLocation;





    private Transactions transactions;


    public Online_Portal(
        String StoreLocation    ) {
        this.StoreLocation = StoreLocation;
    }


    public String getStorelocation() {
        return StoreLocation;
    }

    public void setStorelocation(String StoreLocation) {
        this.StoreLocation = StoreLocation;
    }

    public Transactions getTransactions() {
        return transactions;
    }

    public void setTransactions(Transactions transactions) {
        this.transactions = transactions;
    }

}