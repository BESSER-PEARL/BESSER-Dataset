





import java.util.List;
import java.util.ArrayList;

public class account_Account  {

    private String accountNo;
    private float balance;
    private None type;





    private Customer customer;




    private List<transaction_Transaction> transaction_transactions;


    public account_Account(
        String accountNo,        float balance,        None type    ) {
        this.accountNo = accountNo;
        this.balance = balance;
        this.type = type;
        this.transaction_transactions = new ArrayList<>();
    }

    public account_Account(
        String accountNo,        float balance,        None type        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.accountNo = accountNo;
        this.balance = balance;
        this.type = type;
        this.transaction_transactions = transaction_transactions;
    }

    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }

}