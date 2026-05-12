





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private float balance;
    private String accountNo;
    private None type;





    private List<transaction_Transaction> transaction_transactions;


    public account_Account(
        float balance,        String accountNo,        None type    ) {
        this.balance = balance;
        this.accountNo = accountNo;
        this.type = type;
        this.transaction_transactions = new ArrayList<>();
    }

    public account_Account(
        float balance,        String accountNo,        None type        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.balance = balance;
        this.accountNo = accountNo;
        this.type = type;
        this.transaction_transactions = transaction_transactions;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }

    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }

}