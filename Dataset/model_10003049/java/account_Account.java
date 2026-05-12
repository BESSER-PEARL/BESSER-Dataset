





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String userID;
    private None type;
    private String pin;
    private String accountNum;
    private float balance;





    private List<transaction_Transaction> transaction_transactions;


    public account_Account(
        String userID,        None type,        String pin,        String accountNum,        float balance    ) {
        this.userID = userID;
        this.type = type;
        this.pin = pin;
        this.accountNum = accountNum;
        this.balance = balance;
        this.transaction_transactions = new ArrayList<>();
    }

    public account_Account(
        String userID,        None type,        String pin,        String accountNum,        float balance        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.userID = userID;
        this.type = type;
        this.pin = pin;
        this.accountNum = accountNum;
        this.balance = balance;
        this.transaction_transactions = transaction_transactions;
    }

    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
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
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }

}