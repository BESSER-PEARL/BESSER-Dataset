





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String pin;
    private String accountNum;
    private float balance;
    private None type;
    private String userID;





    private List<transaction_Transaction> transaction_transactions;




    private Profile profile;


    public account_Account(
        String pin,        String accountNum,        float balance,        None type,        String userID    ) {
        this.pin = pin;
        this.accountNum = accountNum;
        this.balance = balance;
        this.type = type;
        this.userID = userID;
        this.transaction_transactions = new ArrayList<>();
    }

    public account_Account(
        String pin,        String accountNum,        float balance,        None type,        String userID        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.pin = pin;
        this.accountNum = accountNum;
        this.balance = balance;
        this.type = type;
        this.userID = userID;
        this.transaction_transactions = transaction_transactions;
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
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }

    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }
    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}