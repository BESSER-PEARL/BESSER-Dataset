





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String accountNum;
    private String userID;
    private float balance;
    private None type;
    private String pin;





    private List<transaction_Transaction> transaction_transactions;


    public account_Account(
        String accountNum,        String userID,        float balance,        None type,        String pin    ) {
        this.accountNum = accountNum;
        this.userID = userID;
        this.balance = balance;
        this.type = type;
        this.pin = pin;
        this.transaction_transactions = new ArrayList<>();
    }

    public account_Account(
        String accountNum,        String userID,        float balance,        None type,        String pin        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.accountNum = accountNum;
        this.userID = userID;
        this.balance = balance;
        this.type = type;
        this.pin = pin;
        this.transaction_transactions = transaction_transactions;
    }

    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }

    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }

}