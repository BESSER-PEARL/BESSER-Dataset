





import java.util.List;
import java.util.ArrayList;

public class Model_WithdrawTransaction  {

    private int amount;



    public Model_WithdrawTransaction(
        int amount    ) {
        this.amount = amount;
    }


    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }


}