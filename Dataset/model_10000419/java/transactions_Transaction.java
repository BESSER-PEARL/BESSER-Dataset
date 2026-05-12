




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class transactions_Transaction  {

    private LocalDate transactionTime;
    private float amount;
    private None type;
    private int id;





    private account_Account account_account;


    public transactions_Transaction(
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

    public account_Account getAccount_account() {
        return account_account;
    }

    public void setAccount_account(account_Account account_account) {
        this.account_account = account_account;
    }

}