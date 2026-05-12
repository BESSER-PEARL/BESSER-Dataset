




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private LocalDate transactionTime;
    private float amount;
    private None type;
    private int id;



    public transaction_Transaction(
        LocalDate transactionTime,        float amount,        None type,        int id    ) {
        this.transactionTime = transactionTime;
        this.amount = amount;
        this.type = type;
        this.id = id;
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