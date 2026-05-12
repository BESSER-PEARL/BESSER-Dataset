





import java.util.List;
import java.util.ArrayList;

public class F1  {

    private float balance;
    private String ownerName;



    public F1(
        float balance,        String ownerName    ) {
        this.balance = balance;
        this.ownerName = ownerName;
    }


    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getOwnername() {
        return ownerName;
    }

    public void setOwnername(String ownerName) {
        this.ownerName = ownerName;
    }


}