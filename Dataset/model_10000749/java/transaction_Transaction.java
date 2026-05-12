




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private int id;
    private float amount;
    private LocalDate transactionTime;
    private None type;





    private account_Account account_account;


    public transaction_Transaction(
        int id,        float amount,        LocalDate transactionTime,        None type    ) {
        this.id = id;
        this.amount = amount;
        this.transactionTime = transactionTime;
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

    public account_Account getAccount_account() {
        return account_account;
    }

    public void setAccount_account(account_Account account_account) {
        this.account_account = account_account;
    }

}