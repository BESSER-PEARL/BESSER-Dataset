




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private float amount;
    private LocalDate transactionTime;
    private int id;
    private None type;



    public transaction_Transaction(
        float amount,        LocalDate transactionTime,        int id,        None type    ) {
        this.amount = amount;
        this.transactionTime = transactionTime;
        this.id = id;
        this.type = type;
    }


    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public LocalDate getTransactiontime() {
        return transactionTime;
    }

    public void setTransactiontime(LocalDate transactionTime) {
        this.transactionTime = transactionTime;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}