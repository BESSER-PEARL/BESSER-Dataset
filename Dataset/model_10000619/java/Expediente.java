





import java.util.List;
import java.util.ArrayList;

public class Expediente  {

    private String ownerName;
    private float balance;



    public Expediente(
        String ownerName,        float balance    ) {
        this.ownerName = ownerName;
        this.balance = balance;
    }


    public String getOwnername() {
        return ownerName;
    }

    public void setOwnername(String ownerName) {
        this.ownerName = ownerName;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }


}