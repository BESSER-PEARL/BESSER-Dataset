




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private LocalDate transactionTime;
    private float amount;
    private int id;
    private None type;



    public Transaction(
        LocalDate transactionTime,        float amount,        int id,        None type    ) {
        this.transactionTime = transactionTime;
        this.amount = amount;
        this.id = id;
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