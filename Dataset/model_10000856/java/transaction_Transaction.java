




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private float amount;
    private LocalDate transactionTime;
    private None type;
    private int id;



    public transaction_Transaction(
        float amount,        LocalDate transactionTime,        None type,        int id    ) {
        this.amount = amount;
        this.transactionTime = transactionTime;
        this.type = type;
        this.id = id;
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


}