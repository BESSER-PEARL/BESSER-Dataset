




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private int id;
    private None type;
    private LocalDate transactionTime;
    private float amount;



    public transaction_Transaction(
        int id,        None type,        LocalDate transactionTime,        float amount    ) {
        this.id = id;
        this.type = type;
        this.transactionTime = transactionTime;
        this.amount = amount;
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
    public LocalDate getTransactiontime() {
        return transactionTime;
    }

    public void setTransactiontime(LocalDate transactionTime) {
        this.transactionTime = transactionTime;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }


}