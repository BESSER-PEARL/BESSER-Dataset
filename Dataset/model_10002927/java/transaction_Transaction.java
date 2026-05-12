




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private LocalDate transactionTime;
    private None type;
    private int id;
    private float amount;



    public transaction_Transaction(
        LocalDate transactionTime,        None type,        int id,        float amount    ) {
        this.transactionTime = transactionTime;
        this.type = type;
        this.id = id;
        this.amount = amount;
    }


    public LocalDate getTransactiontime() {
        return transactionTime;
    }

    public void setTransactiontime(LocalDate transactionTime) {
        this.transactionTime = transactionTime;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }


}