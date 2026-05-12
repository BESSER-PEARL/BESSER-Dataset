




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private LocalDate transactionTime;
    private None type;
    private float amount;
    private int id;





    private Account account;


    public Transaction(
        LocalDate transactionTime,        None type,        float amount,        int id    ) {
        this.transactionTime = transactionTime;
        this.type = type;
        this.amount = amount;
        this.id = id;
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

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}